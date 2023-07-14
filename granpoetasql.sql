-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema elgranpoeta
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema elgranpoeta
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `elgranpoeta` DEFAULT CHARACTER SET utf8 ;
USE `elgranpoeta` ;

-- -----------------------------------------------------
-- Table `elgranpoeta`.`categoria`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`categoria` (
  `idcategoria` INT NOT NULL AUTO_INCREMENT,
  `categoria` VARCHAR(45) NULL,
  PRIMARY KEY (`idcategoria`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idcategoria_UNIQUE` ON `elgranpoeta`.`categoria` (`idcategoria` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`tipoproducto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`tipoproducto` (
  `idtipo` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL,
  PRIMARY KEY (`idtipo`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idtipo_UNIQUE` ON `elgranpoeta`.`tipoproducto` (`idtipo` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`producto`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`producto` (
  `idproducto` INT NOT NULL AUTO_INCREMENT,
  `descripcion` VARCHAR(45) NULL,
  `categoria_idcategoria` INT NOT NULL,
  `tipoproducto_idtipo` INT NOT NULL,
  PRIMARY KEY (`idproducto`),
  CONSTRAINT `fk_producto_categoria`
    FOREIGN KEY (`categoria_idcategoria`)
    REFERENCES `elgranpoeta`.`categoria` (`idcategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_producto_tipoproducto1`
    FOREIGN KEY (`tipoproducto_idtipo`)
    REFERENCES `elgranpoeta`.`tipoproducto` (`idtipo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_producto_categoria_idx` ON `elgranpoeta`.`producto` (`categoria_idcategoria` ASC) ;

CREATE INDEX `fk_producto_tipoproducto1_idx` ON `elgranpoeta`.`producto` (`tipoproducto_idtipo` ASC) ;

CREATE UNIQUE INDEX `idproducto_UNIQUE` ON `elgranpoeta`.`producto` (`idproducto` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`autor` (
  `idautor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idautor`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idautor_UNIQUE` ON `elgranpoeta`.`autor` (`idautor` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`producto_autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`producto_autor` (
  `idproductoautor` INT NOT NULL AUTO_INCREMENT,
  `producto_idproducto` INT NOT NULL,
  `autor_idautor` INT NOT NULL,
  PRIMARY KEY (`idproductoautor`),
  CONSTRAINT `fk_producto_autor_producto1`
    FOREIGN KEY (`producto_idproducto`)
    REFERENCES `elgranpoeta`.`producto` (`idproducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_producto_autor_autor1`
    FOREIGN KEY (`autor_idautor`)
    REFERENCES `elgranpoeta`.`autor` (`idautor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_producto_autor_producto1_idx` ON `elgranpoeta`.`producto_autor` (`producto_idproducto` ASC) ;

CREATE INDEX `fk_producto_autor_autor1_idx` ON `elgranpoeta`.`producto_autor` (`autor_idautor` ASC) ;

CREATE UNIQUE INDEX `idproductoautor_UNIQUE` ON `elgranpoeta`.`producto_autor` (`idproductoautor` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`bodega`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`bodega` (
  `idbodega` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `ubicacion` VARCHAR(45) NULL,
  PRIMARY KEY (`idbodega`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idbodega_UNIQUE` ON `elgranpoeta`.`bodega` (`idbodega` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`copia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`copia` (
  `idcopia` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `producto_idproducto` INT NOT NULL,
  `bodega_idbodega` INT NOT NULL,
  PRIMARY KEY (`idcopia`),
  CONSTRAINT `fk_copia_producto1`
    FOREIGN KEY (`producto_idproducto`)
    REFERENCES `elgranpoeta`.`producto` (`idproducto`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_copia_bodega1`
    FOREIGN KEY (`bodega_idbodega`)
    REFERENCES `elgranpoeta`.`bodega` (`idbodega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_copia_producto1_idx` ON `elgranpoeta`.`copia` (`producto_idproducto` ASC) ;

CREATE INDEX `fk_copia_bodega1_idx` ON `elgranpoeta`.`copia` (`bodega_idbodega` ASC) ;

CREATE UNIQUE INDEX `idcopia_UNIQUE` ON `elgranpoeta`.`copia` (`idcopia` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`tipousuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`tipousuario` (
  `idtipousuario` INT NOT NULL AUTO_INCREMENT,
  `rol` VARCHAR(45) NULL,
  PRIMARY KEY (`idtipousuario`))
ENGINE = InnoDB;

CREATE UNIQUE INDEX `idtipousuario_UNIQUE` ON `elgranpoeta`.`tipousuario` (`idtipousuario` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`usuario` (
  `idusuario` INT NOT NULL AUTO_INCREMENT,
  `telefono` INT NULL,
  `correo` VARCHAR(45) NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `rut` VARCHAR(45) NULL,
  `tipousuario_idtipousuario` INT NOT NULL,
  `contrasena` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idusuario`),
  CONSTRAINT `fk_usuario_tipousuario1`
    FOREIGN KEY (`tipousuario_idtipousuario`)
    REFERENCES `elgranpoeta`.`tipousuario` (`idtipousuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_usuario_tipousuario1_idx` ON `elgranpoeta`.`usuario` (`tipousuario_idtipousuario` ASC) ;

CREATE UNIQUE INDEX `idusuario_UNIQUE` ON `elgranpoeta`.`usuario` (`idusuario` ASC) ;

CREATE UNIQUE INDEX `nombre_UNIQUE` ON `elgranpoeta`.`usuario` (`nombre` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`movimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`movimiento` (
  `idmov` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `usuario_idusuario` INT NOT NULL,
  PRIMARY KEY (`idmov`),
  CONSTRAINT `fk_movimiento_usuario1`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `elgranpoeta`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_movimiento_usuario1_idx` ON `elgranpoeta`.`movimiento` (`usuario_idusuario` ASC) ;

CREATE UNIQUE INDEX `idmov_UNIQUE` ON `elgranpoeta`.`movimiento` (`idmov` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`copia_movimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`copia_movimiento` (
  `idcopiamov` INT NOT NULL AUTO_INCREMENT,
  `copia_idcopia` INT NOT NULL,
  `movimiento_idmov` INT NOT NULL,
  PRIMARY KEY (`idcopiamov`),
  CONSTRAINT `fk_copia_movimiento_copia1`
    FOREIGN KEY (`copia_idcopia`)
    REFERENCES `elgranpoeta`.`copia` (`idcopia`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_copia_movimiento_movimiento1`
    FOREIGN KEY (`movimiento_idmov`)
    REFERENCES `elgranpoeta`.`movimiento` (`idmov`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_copia_movimiento_copia1_idx` ON `elgranpoeta`.`copia_movimiento` (`copia_idcopia` ASC) ;

CREATE INDEX `fk_copia_movimiento_movimiento1_idx` ON `elgranpoeta`.`copia_movimiento` (`movimiento_idmov` ASC) ;

CREATE UNIQUE INDEX `idcopiamov_UNIQUE` ON `elgranpoeta`.`copia_movimiento` (`idcopiamov` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`bodega_movimiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`bodega_movimiento` (
  `idbodegamov` INT NOT NULL AUTO_INCREMENT,
  `estado` TINYINT NULL,
  `movimiento_idmov` INT NOT NULL,
  `bodega_idbodega` INT NOT NULL,
  PRIMARY KEY (`idbodegamov`),
  CONSTRAINT `fk_bodega_movimiento_movimiento1`
    FOREIGN KEY (`movimiento_idmov`)
    REFERENCES `elgranpoeta`.`movimiento` (`idmov`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bodega_movimiento_bodega1`
    FOREIGN KEY (`bodega_idbodega`)
    REFERENCES `elgranpoeta`.`bodega` (`idbodega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_bodega_movimiento_movimiento1_idx` ON `elgranpoeta`.`bodega_movimiento` (`movimiento_idmov` ASC) ;

CREATE INDEX `fk_bodega_movimiento_bodega1_idx` ON `elgranpoeta`.`bodega_movimiento` (`bodega_idbodega` ASC) ;

CREATE UNIQUE INDEX `idbodegamov_UNIQUE` ON `elgranpoeta`.`bodega_movimiento` (`idbodegamov` ASC) ;


-- -----------------------------------------------------
-- Table `elgranpoeta`.`bodega_usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `elgranpoeta`.`bodega_usuario` (
  `idbodegausuario` INT NOT NULL AUTO_INCREMENT,
  `usuario_idusuario` INT NOT NULL,
  `bodega_idbodega` INT NOT NULL,
  PRIMARY KEY (`idbodegausuario`),
  CONSTRAINT `fk_bodega_usuario_usuario1`
    FOREIGN KEY (`usuario_idusuario`)
    REFERENCES `elgranpoeta`.`usuario` (`idusuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_bodega_usuario_bodega1`
    FOREIGN KEY (`bodega_idbodega`)
    REFERENCES `elgranpoeta`.`bodega` (`idbodega`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE INDEX `fk_bodega_usuario_usuario1_idx` ON `elgranpoeta`.`bodega_usuario` (`usuario_idusuario` ASC) ;

CREATE INDEX `fk_bodega_usuario_bodega1_idx` ON `elgranpoeta`.`bodega_usuario` (`bodega_idbodega` ASC) ;

CREATE UNIQUE INDEX `idbodegausuario_UNIQUE` ON `elgranpoeta`.`bodega_usuario` (`idbodegausuario` ASC) ;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
